ang1 = int(input())
ang2 = int(input())
ang3 = int(input())


def ans(ang1, ang2, ang3):
  if ang1 + ang2 + ang3 == 180:
    return True
  else:
    return False


print(ans(ang1, ang2, ang3))