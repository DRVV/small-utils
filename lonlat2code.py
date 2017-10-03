import math
import argparse



def lonlat2code(lon, lat):
    p = math.floor((lat * 60) / 40)

    a = (lat * 60) % 40

    q = math.floor(a / 5)

    b = a % 5

    r = math.floor((b * 60) / 30)

    c = (b * 60) % 30

    s = math.floor(c / 15)

    d = c % 15

    t = math.floor(d / 7.5)

    u = math.floor(lon - 100)

    f = lon - 100 - u

    v = math.floor((f * 60) / 7.5)

    g = (f * 60) % 7.5

    w = math.floor((g * 60) / 45)

    h = (g * 60) % 45

    x = math.floor(h / 22.5)

    i = h % 22.5

    y = math.floor(i / 11.25)

    m = (s * 2) + (x + 1)

    n = (t * 2) + (y + 1)

    # 1    次メッシュ
    mesh = "" + str(p) + str(u)
    # // 2   次メッシュ
    # if resolution >= 2:
    mesh = mesh + str(q) + str(v)
    # // 3次メッシュ
    mesh = mesh + str(r) + str(w)
    # // 1 / 2メッシュ
    mesh = mesh + str(m)
    # 1/4 メッシュ
    mesh = mesh + str(n)

    return mesh


if __name__ == '__main__':
    par = argparse.ArgumentParser()
    par.add_argument('lon')
    par.add_argument('lat')

    args = par.parse_args()
    print(lonlat2code(float(args.lon), float(args.lat)))
    print(lonlat2code(float(args.lat), float(args.lon)))
