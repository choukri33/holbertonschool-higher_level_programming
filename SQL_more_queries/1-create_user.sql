-- 1-create_user.sql

-- Crée l'utilisateur 'user_0d_1' si ce n'est pas déjà fait
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Attribue tous les privilèges à 'user_0d_1' sur toutes les bases de données
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Applique les modifications pour que les changements prennent effet
FLUSH PRIVILEGES;