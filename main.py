import time


def test_func(func):
   def wrapper(*args, **kwargs):
      with open("data.txt", "w", encoding="utf-8") as f:
          res = func(*args, **kwargs)
          f.write(res)
          return res

   return wrapper

@test_func
def sum_fun(a, b, seconds=None):
  x = a + b
  local_time = time.ctime(seconds)
  return f"{local_time}, Сумма двух чисел {a} и {b} равна: {x}"


res = sum_fun(250, 350)



if __name__ == '__main__':
    print(res)
