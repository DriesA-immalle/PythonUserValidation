import click

class StartsNotWithCapitalLetterError(ValueError):
    pass

class NoDigitError(ValueError):
    pass

def validate(userInput):
    if not userInput[0].isupper():
        raise StartsNotWithCapitalLetterError
    if not any(char.isdigit() for char in userInput):
        raise NoDigitError

if __name__ == "__main__":
    userInput = input('>>> ')
    
    try: 
        validate(userInput)
    except StartsNotWithCapitalLetterError:
        click.secho('Input needs to start with a capital letter', fg='red')
    except NoDigitError:
        click.secho('Input needs to contain a digit', fg='red')