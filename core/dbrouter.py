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
        print hints
        
        if model._meta.app_label == 'core' and table == 'profile':
            print model
            instance = hints.get('instance')
            if not instance:
                return 'profile1'
            
            user_id = getattr(instance, 'user_id', None)
            if not user_id:
                return 'profile1'
            
            return 'profile2'
        return None
        
        #if model._meta.app_label == 'core' and table == 'profile':
        #    print 'r', table, model, hints, hints.get('instance')
        #    return 'profile1'
        #return 'default'

    def db_for_write(self, model, **hints):
        table = self.get_model_table_name(model._meta.db_table)
        if model._meta.app_label == 'core' and table == 'profile':
            if hints['instance'].user_id < 11:
                return 'profile1'
            else:
                return 'profile2'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return False

    def allow_syncdb(self, db, model):
        table = self.get_model_table_name(model._meta.db_table)
        if db == 'default' and table == 'profile':
            return False
        if (db == 'profile1' or db == 'profile2') and table != 'profile':
            return False 
        return None