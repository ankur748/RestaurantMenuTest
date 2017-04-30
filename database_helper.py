from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem,User

engine      = create_engine('sqlite:///RestaurantMenu.db')
Base.metadata.bind=engine
DBSession   = sessionmaker(bind = engine)
session     = DBSession()

def create_new_user(name, email, picture):
    user = User(name = name, email = email, picture = picture)
    session.add(user)
    session.commit()

def get_user_by_email(email):
    try:
        user = session.query(User).filter_by(email = email).one()
        return user
    except:
        return None

def get_user_by_id(id):
    return session.query(User).filter_by(id = id).one()

def get_all_restaurants():
    return session.query(Restaurant).all()

def get_one_restaurant(restaurant_id):
    return session.query(Restaurant).filter_by(id = restaurant_id).one()

def edit_one_restaurant(restaurant_id, restaurant_name=""):
    restaurant      = get_one_restaurant(restaurant_id)
    restaurant.name = restaurant_name
    session.add(restaurant)
    session.commit()

def delete_one_restaurant(restaurant_id):
    restaurant      = get_one_restaurant(restaurant_id)
    session.delete(restaurant)
    session.commit()

def create_new_restaurant(restaurant_name, login_session):
    restaurant = Restaurant(name = restaurant_name, user_id = login_session['userid'])
    session.add(restaurant)
    session.commit()

def get_all_menu_items(restaurant_id):
    return session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()

def get_one_menu_item(item_id):
    return session.query(MenuItem).filter_by(id = item_id).one()

def edit_one_menu_item(item_id, item_name = "", item_price = "", item_description = "", item_course = ""):
    item = get_one_menu_item(item_id)

    item.name           = item_name
    item.price          = item_price
    item.description    = item_description
    item.course         = item_course

    session.add(item)
    session.commit()

def delete_one_menu_item(item_id):
    item = get_one_menu_item(item_id)
    session.delete(item)
    session.commit()

def create_new_menu_item(restaurant_id, item_name = "", item_price = "", item_description = "", item_course = ""):
    
    item = MenuItem(name = item_name, price = item_price, description = item_description, course = item_course, restaurant_id = restaurant_id)

    session.add(item)
    session.commit()