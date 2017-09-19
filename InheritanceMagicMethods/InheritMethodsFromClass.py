class Animal:
    def __init__(self, birthType="Unknown", appearance="Unknown", blooded="Unknown"):
        self.__birthType = birthType
        self.__appearance = appearance
        self.__blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A{} is {} it is {} it is {}".format (type (self).__name__, self.birthType, self.appearance,
                                                     self.blooded)


class Mammal (Animal):
    def __init__(self, birthType="born alive", appearance="hair or fur", blooded="warm blooded", nurseYoung=True):
        Animal.__init__ (self, birthType, appearance, blooded)

        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super ().__str__ () + " and it is {} they nurse their young".format (sel)


class Reptile (Animal):
    def __init__(self, birthType="born from egg", appearance="dry scales", blooded="cold blooded"):
        Animal.__init__ (self, birthType, appearance, blooded)

    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += i
        return sum ()

## This is where the input goes
def main():
    animal1 = Animal ("born alive")

    print(animal1.birthType)

    print(animal1)


main ()
