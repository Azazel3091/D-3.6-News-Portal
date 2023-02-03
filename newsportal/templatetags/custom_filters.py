from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
   forbwords = ['припомнили', 'олимпийским', 'спортивную', 'победителю', 'витамины', 'добавки', 'товары', 'поощрение', 'денежного', 'поведению', 'неправильном']

   if not isinstance(value, str):
      raise TypeError(f"Некорректный набор: '{type(value)}'Введите строковое значение")

   for word in value.split():
      if word.lower() in forbwords:
         value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
   # Возвращаемое функцией значение подставится в шаблон.
   return value