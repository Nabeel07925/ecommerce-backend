import inspect


class ForsitEnum(object):
    @classmethod
    def as_list(cls):
        _list = []
        for key, val in cls.__dict__.items():
            if not key.startswith('_') and not inspect.isroutine(val):
                _list.append(val)
        return _list


class UserStatus(ForsitEnum):
    UN_REGISTERED = 'un-registered'
    UN_VERIFIED = 'un-verified'
    VERIFIED = 'verified'


class OrderState(ForsitEnum):
    PENDING_CHECKOUT = 'pending-checkout'
    PENDING_PAYMENT = 'pending-payment'
    SHIPPING_WITH_PAYMENT = 'shipping-with-payment'
    SHIPPING_WITHOUT_PAYMENT = 'shipping-without-payment'
    COMPLETED = 'completed'


class ProductCategoryCodes(ForsitEnum):
    ENTERTAINMENT = 'entertainment'
    DECOR = 'decor'
    DIGITAL = 'digital'
    FOOD = 'food'
    FURNITURE = 'furniture'
    HEALTH = 'health'
    HOUSE_HOLD = 'house_hold'
    MEDIA = 'media'
    PET_CARE = 'pet_care'
    OFFICE = 'office'
    OTHER = 'other'

