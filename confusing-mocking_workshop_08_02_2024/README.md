# Mocking workshop 08 02 2024

Setup instructions:
```
$ git clone git@github.com:tamasmagyarhunor-makers/mocking_workshop_08_02_2024.git
$ cd mocking_workshop_08_02_2024
$ pipenv intall
$ pipenv run pytest -xv
```

Instructions:
- please update the design_recipe with the following user story
```
As a Business Stakeholder
I would like the Fruit class to return the calory of a Fruit as a String
So its more readable to our customers. eg. 'This [fruit_name] has [calory] calories'
```
- Please update tests for this new requirement and concentrate only on the Fruit class and Fruit tests. You can run ONLY the Fruit tests with `pipenv run pytest -xv tests/test_fruit.py`
- Once your new Fruit tests run and pass, so the user story is now implemented, please run all your tests `pipenv run pytest -xv` and notice how now your Blender tests starts failing. You can stop at this point, we will continue in the workshop.

tip: you can simply update your `get_calories()` function.