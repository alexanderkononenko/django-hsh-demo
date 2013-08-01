import re


class ShardingRouter(object):
    """
    A router to control all database operations on models in the
    core application.
    """ 
    def get_model_table_name(self, model):
        r = re.search('core_(user|profile)', model)
        if r:
            return r.group(1)
        else:
            return False

    def db_for_read(self, model, **hints):
        table = self.get_model_table_name(model._meta.db_table)
        print 'r', table, model, hints
        #return False
        if model._meta.app_label == 'Profile':
            return 'profile1'
        return 'default'

    def db_for_write(self, model, **hints):
        table = self.get_model_table_name(model._meta.db_table)
        z = hints['instance']
        print 'w', table, model, z, z.id
        if model._meta.app_label == 'Profile':
            return 'profile1'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'chinook' and obj2._meta.app_label == 'chinook':
            return True
        # Allow if neither is chinook app
        elif 'chinook' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False

    def allow_syncdb(self, db, model):
        table = self.get_model_table_name(model._meta.db_table)
        if db == 'default' and table == 'profile':
            return False
        if (db == 'profile1' or db == 'profile2') and table != 'profile':
            return False 
        return None