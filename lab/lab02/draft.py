def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

chocolate = cake()
more_chocolate, more_cake = chocolate(), cake