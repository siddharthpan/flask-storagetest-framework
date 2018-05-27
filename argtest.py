import sys

tgt = sys.argv[0]
def main():
    if tgt == 'sdcard':
        print('SDCARD')
    elif tgt == 'pendrive':
        print('PENDRIVE')
    return None

if __name__ == '__main__':
    main()