#### 1. Authentification sur Azure

Connectez-vous à Azure CLI :

```
az login
```

#### 2. Configuration de l'Abonnement Azure

Sélectionne l'abonnement en utilisant son ID :

```
az account set --subscription 974386b8-dfe6-43cc-94af-17335974d64a
```

#### 3. Création d'un Registre de Conteneurs Azure (ACR)

Crée un ACR dans le groupe de ressources `SimplonDevIA`  :

```
az acr create --resource-group SimplonDevIA --name [VotreNomRegistry] --sku Basic
```
Remplace `[VotreNomRegistry]` par le nom que tu souhaites donner au registre de conteneurs

#### 4. Push de l'Image sur ACR

Après avoir construit l'image Docker, connecte-toi à ACR :

```
az acr login --name [VotreNomRegistry]
```

Tagge et pousse l'image Docker :

```
docker tag nom_app:tag [VotreNomRegistry].azurecr.io/nom_app:tag
docker push [VotreNomRegistry].azurecr.io/nom_app:tag
```

#### 5. Déploiement sur Azure

7. Déploiement sur Azure App Service ou Azure Kubernetes Service (AKS)

Pour Azure App Service:
Créez un App Service Plan:

```
az appservice plan create --name monAppServicePlan --resource-group SimplonDevIA --is-linux
```

Déploye l'application:

```
az webapp create --resource-group SimplonDevIA --plan monAppServicePlan --name monAppName --deployment-container-image-name nomRegistry.azurecr.io/nom_app:tag
```

Pour Azure Kubernetes Service:
Crée un cluster AKS (si nécessaire):

```
az aks create --resource-group SimplonDevIA --name monAKSCluster --node-count 1 --enable-addons monitoring --generate-ssh-keys
```

Connecte-toi au cluster:

```
az aks get-credentials --resource-group nom_groupe_ressources --name monAKSCluster
```

Déploye l'application sur AKS:

Utilise un fichier deployment.yaml pour configurer le déploiement sur AKS et applique-le avec kubectl apply -f deployment.yaml

