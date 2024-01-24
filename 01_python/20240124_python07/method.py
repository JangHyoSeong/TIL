class Myclass:

  def instance_method(self):
    return 'instance method', self

  @classmethod
  def class_method(cls):
    return 'class method', cls

  @staticmethod
  def static_method():
    return 'static method'


instance = Myclass()

# 클래스가 전부 호출하기
print(Myclass.instance_method(instance))
print(Myclass.class_method())
print(Myclass.static_method())
# 에러 안남

# 인스턴스가 전부 호출하기
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())
# 에러 안남
# 본인한테 없는 메서드여도 찾아올라감. 가능하지만 쓰지는 말자