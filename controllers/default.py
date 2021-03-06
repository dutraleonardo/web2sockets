from gluon.contrib.websocket_messaging import websocket_send


@auth.requires_login()
def index():
    form = SQLFORM(Post, formstyle='divs')
    if form.process().accepted:
        session.flash = 'form accepted'
        js = "jQuery('.new').slideDown('slow')"
        websocket_send('http://127.0.0.1:8888', js, "chatkey", "mygroup")
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    messages = db(Post).select(orderby=~Post.created_on)

    return dict(form=form,messages=messages)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


