
class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty.")
        setattr(instance, self.name, value.strip())


class EmailDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Email must contain @.")
        setattr(instance, self.name, value.strip())


class AgeDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("Age must be an integer.")
        if not 16 <= value <= 80:
            raise ValueError("Age must be between 16 and 80.")
        setattr(instance, self.name, value)
