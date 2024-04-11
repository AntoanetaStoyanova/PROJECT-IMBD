Step by step

1. Création d'un fichier Dockerfile
    Place le Dockerfile à la racine du projet
    
FROM node:14
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]


2. Construction de l'image Docker
    Création de l'image Docker de l'application localement en utilisant la commande:

docker build -t nom_app:tag .

    nom_app est le nom de l'application et tag la version spécifique de l'image
    
3. Testez l'Image Localement
    Après avoir construit l'image, teste la localement:
docker run -p 4000:3000 nom_app:tag

    Cela démarre un conteneur Docker de l'application accessible sur le port 4000 de ta machine en local