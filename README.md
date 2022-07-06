# online-kuharica

# Web projekt Online Kuharica

# Backend

```
------VIRTUAL ENVIRONMENT------
cd backend
virtualenv venv
venv\Scripts\activate.ps1
pip install -r requirements.txt

------SERVER-------
$env:FLASK_APP="kuharica"
$env:FLASK_ENV="development"
flask run
```

# Podesiti lokaciju venv foldera u VS Codeu-u

```
File > Preferences > Settings > Python: Venv Path
${workspaceFolder}\online-kuharica\backend\venv
```

```
python main.py
```

# Frontend


```
npm install
```

### Pokreni server za frontend

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).
