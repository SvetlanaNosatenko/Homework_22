class Unit:
    # ...
    def move_unit(self, field, x, y, direction, fly, crawl, speed=1):

        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            speed *= 1.2   # сцепления наших тапочек с землей нет, трение меньше, поэтому скорость выше
            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)