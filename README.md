# Exemple de superset via docker

Cette image est composée des services suivants :

* superset (accessible sur [http://localhost:8088](http://localhost:8088))
* redis
* postgres
* pgadmin

### Cloner le répertoire git
```bash
git clone https://framagit.org/lejedi76/dvf-superset.git
```

### Démarrer les services redis et postgres

```
docker-compose up -d redis postres
```

### Démarrer le service superset
```
docker-compose up -d superset
```

### Initialiser superset après un peu d'attente (30s à 1 min)
```
docker exec -ti dvfsuperset_superset_1 superset-init
```

### Pour stoper l'ensemble des services
```
docker-compose down
```
ou

```
#stopper les services et supprimer les volumes associés
docker-compose down -v
```

### Pour relancer les services
```
docker-compose up -d
```
