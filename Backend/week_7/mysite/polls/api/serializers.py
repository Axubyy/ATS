
from asyncore import read
from secrets import choice
from polls.models import Choice, Question
from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.Serializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username',  'email', 'password', 'password2')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def validate(self, attrs):
        if not attrs.get('password') == attrs.get('password2'):
            raise serializers.ValidationError("Passwords doesn't match!")
        return attrs

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Email already in use")
        return lower_email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ChoiceListSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Choice
        fields = "__all__"

    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        instance.choice_text = validated_data.get(
            'choice_text', instance.choice_text)
        instance.votes = validated_data.get(
            'votes', instance.votes)
        return instance


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choice = ChoiceListSerializer(many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        choices = validated_data.pop('choice', [])
        question = Question.objects.create(**validated_data)
        for choice in choices:
            cho = Choice.objects.create(question=question, **choice)
        return question
        return super(Question, self).create(**validated_data)

    # def up(self,instance,validated_data):
    #     email = validated_data.pop('email', None)
    #     return super().up(instance,validated_data)

    def update(self, instance, validated_data):
        choices_data = validated_data.pop('choice')
        choices = (instance.choice).all()
        print(choices)
        choices = list(choices)
        instance.question_text = validated_data.get(
            'question_text', instance.question_text)
        instance.save()

        for choice_data in choices_data:
            choice = choices.pop(0)
            choice.choice_text = choice_data.get(
                'choice_text', choice.choice_text)
            choice.votes = choice_data.get(
                'votes', choice.votes)
            choice.save()
        instance.save()
        return instance

      # def update(self, instance, validated_data):
    #     question = instance
    #     question.__dict__.update(validated_data)
    #     question.save()
    #     return question

        #  {

        #     "choice": [
        #         {

        #             "choice_text": "Ewa",
        #             "votes": 2

        #         },
        #         {

        #             "choice_text": "Garri",
        #             "votes": 1

        #         },
        #         {

        #             "choice_text": "Cassava",
        #             "votes": 0

        #         }
        #     ],
        #     "question_text": "How are you?"

        # }


# {

#     "choice": [{
#         "choice_text": "Backend",
#     },
#         {
#         "choice_text": "Frontend",
#     }],
#     "question_text": "Whats your Track",
# }


# try:
#                 choice = Choice.objects.get(pk=choice_data['id'])
#             except Choice.DoesNotExist:
#                 print("Choice %s not found" % choice_data)

#             choice.choice_text = choice_data.get(
#                 'choice_text', choice.choice_text)

#             choice.save()
