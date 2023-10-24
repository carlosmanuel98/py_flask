/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80030 (8.0.30)
 Source Host           : localhost:3306
 Source Schema         : importacion_test_2

 Target Server Type    : MySQL
 Target Server Version : 80030 (8.0.30)
 File Encoding         : 65001

 Date: 17/10/2023 12:11:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;


-- ----------------------------
-- Table structure for sys_usuarios
-- ----------------------------
DROP TABLE IF EXISTS `sys_usuarios`;
CREATE TABLE `sys_usuarios`  (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `last_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `age` int NULL DEFAULT NULL,
  `gender` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_user`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_usuarios
-- ----------------------------
INSERT INTO `sys_usuarios` VALUES (2, 'carlos', 'Rojas', 50, 'M');
INSERT INTO `sys_usuarios` VALUES (3, 'carlos', 'Rojas', 50, 'M');
INSERT INTO `sys_usuarios` VALUES (6, 'carlos2', 'Perez', 18, 'M');
INSERT INTO `sys_usuarios` VALUES (7, 'carlos2', 'Perez', 18, 'M');
INSERT INTO `sys_usuarios` VALUES (8, 'carlos2', 'Rojas', 18, 'M');
INSERT INTO `sys_usuarios` VALUES (24, 'carlos2', 'Perez', 18, 'M');
INSERT INTO `sys_usuarios` VALUES (25, 'carlos2', 'Rojas', 18, 'M');
INSERT INTO `sys_usuarios` VALUES (27, 'carlosmanuel', 'Rojas1', NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
