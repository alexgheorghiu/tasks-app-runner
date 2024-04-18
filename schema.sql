DROP DATABASE IF EXISTS task_logger;

create database task_logger;

DROP USER IF EXISTS task_logger;

CREATE USER IF NOT EXISTS 'task_logger'@'localhost' IDENTIFIED BY 'task_logger';

GRANT ALL PRIVILEGES ON task_logger.* TO 'task_logger'@'localhost' WITH GRANT OPTION;

USE task_logger;

CREATE TABLE `tasks` (  
    `id` int(11) NOT NULL AUTO_INCREMENT,  
    `title` varchar(255) NOT NULL,  
    `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    PRIMARY KEY (`id`),  
    KEY `created` (`created`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 