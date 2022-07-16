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
            # time_in_seconds = seconds// 60
            self.__second = self.getSecond()
            self.__minute = self.getMinute()
            self.__hour = self.getHour()
            if self.__second > 59 and self.__minute < 59 and self.__hour < 23:
                tick_time = ""
                self.__second = 00
                self.__minute += 1
                tick_time  = f"{self.__hour}0: {self.__minute}0 :{self.__second}0"
            elif self.__minute > 59 and self.__second > 59 and self.__hour != 23:
                self.__minute = 00
                self.__second = 00
                tick_time = f"{self.__hour+1}: {self.__minute} :{self.__second}"
        
            elif self.__minute == 00 and self.__second == 00 or self.__hour == 00:
                tick_time = f"{self.__hour+1}: {self.__minute+1} :{self.__second+1}"
            print(tick_time)
            return tick_time
        
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


# t1 = Time()


t2 = Time(20,59,59)
t = Time(16,30,59)

# t1.setHour( 23 )
# t1.setMinute( 59 )
t2.setSecond( 59 )
print(t2.getHour())
# print(t1.tick())
t.setSecond( 59 )
print(t.tick())
print(t2.tick())
print(t2.printStandard())
# print(t2.tick())
# print(t2.tick())
# print(t2.getHour)

# t3 = Time(23,59,59)
# print(t3.printStandard())