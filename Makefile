create-db:
	FLASK_APP=manage FLASK_ENV=$(ENV) pipenv run flask create-db

drop-db:
	FLASK_APP=manage FLASK_ENV=$(ENV) pipenv run flask drop-db

seed:
	FLASK_APP=manage FLASK_ENV=$(ENV) pipenv run flask seed