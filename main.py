import click

class TooShortError(ValueError):
    pass

class StartsNotWithCapitalLetterError(ValueError):
    pass

class NoDigitError(ValueError):
    pass

def validate(userInput):
    if not len(userInput) > 10:
        raise TooShortError
    if not userInput[0].isupper():
        raise StartsNotWithCapitalLetterError
    if not any(char.isdigit() for char in userInput):
        raise NoDigitError
    else:
        click.secho('Data validated', fg='green')

if __name__ == "__main__":
    validated = False
    while not validated:
        userInput = input('>>> ')
        if click.confirm(f'Do you want to continue with {userInput} as input?'):
            validated = True
            try: 
                validate(userInput)
            except TooShortError:
                click.secho('Input needs to be at least 10 characters long', fg='red')
            except StartsNotWithCapitalLetterError:
                click.secho('Input needs to start with a capital letter', fg='red')
            except NoDigitError:
                click.secho('Input needs to contain a digit', fg='red')
        elif not click.confirm:
            break
