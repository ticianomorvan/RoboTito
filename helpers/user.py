import nextcord


def get_roles(user: nextcord.User):
    roles = user.roles
    roles_string = ''
    for role in roles:
        if len(roles) > 2:
            if role.name != '@everyone':
                roles_string += f'<@&{role.id}> | '
            else:
                pass
        else:
            if role.name != '@everyone':
                return f'<@&{role.id}>'

    return roles_string
