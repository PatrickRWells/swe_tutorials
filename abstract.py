from abc import ABC, abstractmethod



class MyAbstractClass(ABC):
    """
    An abstract base class (ABC) is a class that is designed to only
    be used as a base class for other classes. By inheriting from ABC,
    you tell Python that it is not meant to be created on its own.
    If you try to create an actual object of type MyAbstractClass, for example:

    >>> my_object = MyAbstractClass()

    You will get an error. Instead, you must create a subclass that inherits
    from MyAbstractClass.

    Abstract classes are a sort of "contract" about how certain kinds of objects
    will behave in your code. By using the abc module, we can "enforce" this contract,
    making it less likely that new subclasses will break the code. If you create a 
    subclass that does NOT implement this contract, you will get an error as soon
    as you try to create an object, rather than just when you try to use the object.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def some_important_behavior(self, *args, **kwargs):
        """
        This is an abstract method. All abstract classes should include
        at least one of these (otherwise, there's no point to making a base class)
        If you create a subclass that does not implement this method, you will 
        get an error. This is a good way of defining a particular set of behavior 
        your subclass MUST implement in order to work properly in your code. 

        You don't need to define any behavior here, just write "pass" in the body of the
        function.
        """
        pass
    
        
    def yet_another_behavior(self, *args, **kwargs):
        """
        Abstract classes can still define regular methods. If you create a subclass that does
        not implement this function, you will not get an error and and the subclass will just
        run this code. 
        """
        return "This is a regular method."
    
class MyBrokenClass(MyAbstractClass):
    """
    This class inherits from the abstract class, but doesn't implement
    the abstract method. Creating an object of this class will result in an error.
    """
    def __init__(self, a):
        self.a = a

class MyRealClass(MyAbstractClass):
    """
    This class inherits from the abstract class, defines the required method
    and overrides the regular method. You should be able to create a MyRealClass
    object without any errors.
    """
    def __init__(self, a):
        self.a = a

    def some_important_behavior(self, *args, **kwargs):
        return self.a
    
    def yet_another_behavior(self, *args, **kwargs):
        return "Actually, the subclass is in charge!"
    