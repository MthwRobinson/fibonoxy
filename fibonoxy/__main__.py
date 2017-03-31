import click
from fibonoxy import fibonoxy

@click.group()
def main():
    """
    Welcome to the Fibonoxy CLI!

    To build a heard, use the following command

    $ fibonoxy herd -n 5
    """
    pass

@click.command('herd', help='builds a fantastic ox herd!')
@click.option('-n', default=1, help='number in the fibo sequence')
def herd(n):
    print(fibonoxy(n))
main.add_command(herd)

if __name__ == '__main__':
    main()
