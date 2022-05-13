img:
		docker build -t recipes --no-cache --platform linux/arm/v7 .

tag: img
		docker tag recipes registry.digitalocean.com/arcs/recipes

docker: tag
		docker push registry.digitalocean.com/arcs/recipes