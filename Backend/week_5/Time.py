# Fig: 7.13: Time3.py
# Class Time with default constructor.
class Time:
        """Class Time with default constructor"""
        def __init__( self, hour = 0, minute = 0, second = 0 ):
            """Time constructor initializes each data member to zero"""
            self.setTime( hour, minute, second )
            
        def setTime( self, hour, minute, second ):
            """Set values of hour, minute, and second"""
            self.setHour( hour )
            self.setMinute( minute )
            self.setSecond( second )
        def setHour( self, hour ):
            """Set hour value"""
            if 0 <= hour < 24:
                self.__hour = hour
            else:
                raise ValueError("Invalid hour value: %d" % hour)
            
        def setMinute( self, minute ):
            """Set minute value"""
            if 0 <= minute < 60:
                self.__minute = minute
            else:
                raise ValueError("Invalid minute value: %d" % minute)
            
        def setSecond(self, second):
            """Set second value"""
            if  0 <=second < 60:
                self.__second = second
            else:
                raise ValueError("Invalid second value: %d" % second)
            
        def getHour( self ):
            """Get hour value"""
            return self.__hour

        def getMinute( self ):
            """Get minute value"""
            return self.__minute
        def tick(self):
            """Increment time-in-seconds by a second"""
            print('In Tick..')
            print(self.getSecond())
            increased_time = self.getSecond() + 1
            # print(increased_time)
            return increased_time
        def getSecond( self ):
            """Get second value"""
            return self.__second
        
        def printMilitary( self ):
            """Prints Time object in military format"""
            print(self.__hour, self.__minute, self.__second)
            
        def printStandard( self ):
            """Prints Time object in standard format"""
            standardTime = ""
            if self.__hour == 0 or self.__hour == 12:
                standardTime += "12:"
            else:
                standardTime += "%d:" % ( self.__hour % 12 )
                standardTime += "%.2d:%.2d" % ( self.__minute, self.__second )
            if self.__hour < 12:
                standardTime += " AM"
            else:
                standardTime += " PM"
                print(standardTime)


t1 = Time()


t2 = Time(23,59,59)
# print(t2.tick())
# print(t2.getHour())
# print(t2.tick())
# print(t2.getHour)

# t1.setHour( 23 )
# t1.setMinute( 59 )
# t1.setSecond( 59 )
# print(t1.tick())
print(t2.tick())
# print(t2.printStandard())

# t3 = Time(23,59,59)
# print(t3.printStandard())