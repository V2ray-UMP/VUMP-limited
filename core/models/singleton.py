from core.models import BaseModel

from django.core.validators import ValidationError


class SingletonModel(BaseModel):
    SINGLETON_INSTANCE_ID = 1

    def save(self, *args, **kwargs):
        if (
            (self.pk and self.pk == SingletonModel.SINGLETON_INSTANCE_ID)
            or (not self.pk and not self.__class__.objects.all().exists())
        ):
            return super(SingletonModel, self).save(*args, **kwargs)
        else:
            raise ValidationError('Only one instance of singleton models can be instantiated.')

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=cls.SINGLETON_INSTANCE_ID)
        return obj

    class Meta:
        abstract = True
