class ShardingRouter(object):
    """
    A router to control all database operations on models in the
    core application.
    """
    def db_for_read(self, model, **hints):
        #TODO Can't determine suitable database yet
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'core' and model.__name__ == 'Profile':
            if hints['instance'].user_id < 11:
                return 'profile1'
            else:
                return 'profile2'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return False

    def allow_syncdb(self, db, model):
        if db == 'default' and model.__name__ == 'Profile':
            return False
        if (db == 'profile1' or db == 'profile2') and model.__name__ != 'Profile':
            return False
        return None
