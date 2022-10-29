import time

path = "data.txt"
def parametrized_decor(path):
    def test_func(func):
       def wrapper(*args, **kwargs):
          with open(path, "w", encoding="utf-8") as f:
              res = func(*args, **kwargs)
              f.write(res)
              return res

       return wrapper
    return test_func

@parametrized_decor(path)
def sum_fun(a, b, seconds=None):
  x = a + b
  local_time = time.ctime(seconds)
  return f"{local_time}, Сумма двух чисел {a} и {b} равна: {x}"





if __name__ == '__main__':
    res = sum_fun(250, 350)
    print(res)
