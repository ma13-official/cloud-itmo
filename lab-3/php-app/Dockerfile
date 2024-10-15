FROM php:8.0-apache
RUN apt-get update && apt-get install -y \
    libzip-dev \
    libpng-dev \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install zip \
    && docker-php-ext-install gd
COPY ./index.php /var/www/html/