from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="anonymous", email='anonymous@example.com')
session.add(user1)
session.commit()

# Items for Grass
category1 = Category(name="Grass", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Bulbasaur", user_id=1,
                     description="Bulbasaur is a Grass/Poison type Pokemon" +
                                 "introduced in Generation 1. It is known as" +
                                 "the 'Seed Pokemon'.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Ivysaur", user_id=1,
                     description="Ivysaur is a Grass/Poison type Pokemon" +
                                 "introduced in Generation 1. It is known as" +
                                 "the 'Seed Pokemon'.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Venusaur", user_id=1,
                     description="Venusaur is a Grass/Poison type Pokemon" +
                                 "introduced in Generation 1. It is known as" +
                                 "the 'Seed Pokemon'. Venusaur has a Mega" +
                                 "Evolution, available from X & Y onwards.",
                     category=category1)

session.add(item3)
session.commit()

# Items for Fire
category2 = Category(name="Fire", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Charmander", user_id=1,
                     description="Charmander is a Fire type Pokemon" +
                                 "introduced in Generation 1. It is known" +
                                 "as the 'Lizard Pokemon'.",
                     category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Charmeleon", user_id=1,
                     description="Charmeleon is a Fire type Pokemon" +
                                 "introduced in Generation 1. It is known as" +
                                 "the 'Flame Pokemon'.", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Charizard", user_id=1,
                     description="Charizard is a Fire/Flying type Pokemon" +
                                 "introduced in Generation 1. It is known as" +
                                 "the 'Flame Pokemon'. Charizard has two" +
                                 "Mega Evolutions, available from X & Y" +
                                 "onwards.", category=category2)

session.add(item3)
session.commit()

# Items for Water
category3 = Category(name="Water", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Squirtle", user_id=1,
                     description="Squirtle is a Water type Pokemon" +
                                 "introduced in Generation 1. It is known as" +
                                 "the 'Tiny Turtle Pokemon'.",
                     category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Wartortle", user_id=1,
                     description="Wartortle is a Water type Pokemon" +
                                 "introduced in Generation 1. It is known as" +
                                 "the 'Turtle Pokemon'.", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Blastoise", user_id=1,
                     description="Blastoise is a Water type Pokemon" +
                                 "introduced in Generation 1. It is known" +
                                 "as the 'Shellfish Pokemon'. Blastoise" +
                                 "has a Mega Evolution, available from X" +
                                 "& Y onwards.", category=category3)

session.add(item3)
session.commit()

# Items for Electric
category4 = Category(name="Electric", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Pikachu", user_id=1,
                     description="Pikachu is an Electric type Pokemon" +
                                 "introduced in Generation 1. It is known as" +
                                 "the 'Mouse Pokemon'.", category=category4)

session.add(item1)
session.commit()

# Items for Poison
category5 = Category(name="Poison", user_id=1)
session.add(category5)
session.commit()

# Items for Psychic
category6 = Category(name="Psychic", user_id=1)
session.add(category6)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
