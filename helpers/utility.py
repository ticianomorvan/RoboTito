import datetime


def datetime_parser(date: datetime.datetime):
    """Returns a date in format: day/month/year"""
    return f'{date.day}/{date.month}/{date.year}'


# server invites — utility

def invite_uses(current_uses: int, max_uses: int):
    """Returns the current uses and the maximum uses from an invite"""
    if max_uses == 0:
        return f'{current_uses} uses from a non-limited maximum.'
    else:
        return f'{current_uses} uses from a maximum of {max_uses}'


def invite_expire(date: datetime.datetime):
    if not date:
        return 'This invite doesn\'t expire.'
    else:
        return datetime_parser(date)
