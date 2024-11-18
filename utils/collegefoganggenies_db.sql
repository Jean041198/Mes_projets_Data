-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 18 nov. 2024 à 19:51
-- Version du serveur :  10.4.11-MariaDB
-- Version de PHP : 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `collegefoganggenies_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `administrateur_principal`
--

CREATE TABLE `administrateur_principal` (
  `id` int(11) NOT NULL,
  `identifiant` varchar(100) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `administrateur_principal`
--

INSERT INTO `administrateur_principal` (`id`, `identifiant`, `mot_de_passe`) VALUES
(1, 'adminprincipal123', 'password789');

-- --------------------------------------------------------

--
-- Structure de la table `administration`
--

CREATE TABLE `administration` (
  `id` int(11) NOT NULL,
  `identifiant` varchar(100) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL,
  `nom` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `administration`
--

INSERT INTO `administration` (`id`, `identifiant`, `mot_de_passe`, `nom`) VALUES
(1, 'admin123', 'password123', 'Administrateur');

-- --------------------------------------------------------

--
-- Structure de la table `classes`
--

CREATE TABLE `classes` (
  `nom_de_la_classe` varchar(50) NOT NULL,
  `annee_scolaire` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `classes`
--

INSERT INTO `classes` (`nom_de_la_classe`, `annee_scolaire`) VALUES
('4ème', '2024-2025'),
('5ème', '2024-2025'),
('6ème', '2024-2025'),
('Form1', '2024-2025'),
('Form2', '2024-2025'),
('Form3', '2024-2025');

-- --------------------------------------------------------

--
-- Structure de la table `eleves`
--

CREATE TABLE `eleves` (
  `matricule_eleve` varchar(50) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `classe` varchar(50) NOT NULL,
  `sexe` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `eleves`
--

INSERT INTO `eleves` (`matricule_eleve`, `nom`, `prenom`, `classe`, `sexe`) VALUES
('CBFG01AA', 'Ngoue', 'Nolan', 'Form1', 'M'),
('CBFG01AF', 'Ndongo Sossabéna', 'Daniel Prestanne', '6ème', 'M'),
('CBFG01BA', 'Bomossotie', 'Celestine Rachel', 'Form2', 'F'),
('CBFG01BF', 'Dzukou Guiakam', 'Ange Megane', '5ème', 'F'),
('CBFG01CA', 'Ekouma Mengata', 'Anne Sara', 'Form3', 'F'),
('CBFG01CF', 'Mengbwa', 'Jade Oriane', '4ème', 'F'),
('CBFG02AA', 'Zebaze', 'Iness', 'Form1', 'F'),
('CBFG02AF', 'Bounoung Avebe', 'Hervé Ismae', '6ème', 'M'),
('CBFG02BA', 'Minkoulou Ndegue', 'Jacqueline Talia', 'Form2', 'F'),
('CBFG02BF', 'Sokeng Tsopmo', 'Wesley', '5ème', 'M'),
('CBFG02CA', 'Yogo Mengata', 'Amadae Mireille', 'Form3', 'F'),
('CBFG02CF', 'Kamdem Guiakam', 'Gilles Perrin', '4ème', 'F'),
('CBFG03AA', 'Nkolo', 'Brayan', 'Form1', 'M'),
('CBFG03AF', 'Mballa Ondoua', 'André Jovial', '6ème', 'M'),
('CBFG03BA', 'Mewali Ndegue', 'Jean Baptiste', 'Form2', 'M'),
('CBFG03CA', 'Mballa', 'Sabine Carla', 'Form3', 'F'),
('CBFG03CF', 'Nyangon Aba', 'Mori Julia', '4ème', 'F'),
('CBFG04AA', 'Biem Jean', 'Sylvain Ludivine', 'Form1', 'F'),
('CBFG04AF', 'Dimala', 'Dieudonné', '6ème', 'M'),
('CBFG04BA', 'Mani Laurent', 'Camron', 'Form2', 'M'),
('CBFG04CA', 'Ondoa Halla', 'Ange Stanley', 'Form3', 'M'),
('CBFG05AA', 'Thankgod', 'Massoda', 'Form1', 'M'),
('CBFG05AF', 'Ateba Toulou', 'Christian', '6ème', 'M'),
('CBFG05BA', 'Ngo Bayem', 'Louise', 'Form2', 'F'),
('CBFG05CA', 'Assala', 'Bryan Cabriel', 'Form3', 'M'),
('CBFG06AA', 'Awoumou Ondoa', 'Lagloire', 'Form1', 'F'),
('CBFG06AF', 'Mboe Manga', 'Saintiche Virginie', '6ème', 'F'),
('CBFG06CA', 'Bayem', 'Marie Pascaline', 'Form3', 'F'),
('CBFG07AA', 'Minkoumou', 'Raymond Christian', 'Form1', 'M'),
('CBFG07AF', 'Kenne', 'Forlan Kenzo', '6ème', 'M'),
('CBFG07CA', 'Aboudi', 'Ondoa Esther', 'Form3', 'F'),
('CBFG08AA', 'Louleko', 'Merveille', 'Form1', 'F'),
('CBFG08AF', 'KEWE', 'Dieunedort', '6ème', 'M'),
('CBFG09AA', 'Ndifon', 'Valentin', 'Form1', 'M'),
('CBFG10AA', 'Mbolo', 'Mvondo Pauline', 'Form1', 'F'),
('CBFG11AA', 'Enyegue Foe', 'Juste Dakin', 'Form1', 'M'),
('CBFG12AA', 'Ngah', 'Mangas blaise', 'Form1', 'M');

-- --------------------------------------------------------

--
-- Structure de la table `enseignants`
--

CREATE TABLE `enseignants` (
  `id` int(11) NOT NULL,
  `identifiant` varchar(100) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL,
  `nom` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `enseignants`
--

INSERT INTO `enseignants` (`id`, `identifiant`, `mot_de_passe`, `nom`) VALUES
(126, 'CBFG02PFF', 'password456', 'Gorgia Stéphanie'),
(127, 'CBFG05PFM', 'password456', 'Kongomatchi'),
(128, 'CBFG07PFF', 'password456', 'Ebogo Zana'),
(129, 'CBFG10PFM', 'password456', 'Nyoungou Jean'),
(130, 'CBFG09PFM', 'password456', 'Etokolo Freddy'),
(131, 'CBFG04PFF', 'password456', 'Kossene Ghislaine'),
(132, 'CBFG01PFF', 'password456', 'Ngo Ngimbous Bernadette'),
(133, 'CBFG08PFM', 'password456', 'NGAH'),
(134, 'CBFG03PFF', 'password456', 'Pemboura Aline'),
(135, 'CBFG03PAF', 'password456', 'Tambe Sylvie Orock'),
(136, 'CBFG04PAF', 'password456', 'Ebassa Mireille'),
(137, 'CBFG01PAM', 'password456', 'Ndengue Jude'),
(138, 'CBFG06PAM', 'password456', 'biguin'),
(139, 'CBFG07PAM', 'password456', 'Betty'),
(140, 'CBFG05PAF', 'password456', 'Mariette'),
(141, 'CBFG02PAM', 'password456', 'Bella Ongolo'),
(142, 'CBFG06PFM', 'password456', 'Yeyap Kamdem'),
(143, 'CBFG11PFAM', 'password456', 'Mbida'),
(144, 'CBFG08PAM', 'password456', 'Kemo Elysée'),
(145, 'CBFG09PAM', 'password456', 'NOUKI');

-- --------------------------------------------------------

--
-- Structure de la table `enseignants_classes`
--

CREATE TABLE `enseignants_classes` (
  `id` int(11) NOT NULL,
  `identifiant_enseignant` varchar(100) NOT NULL,
  `nom_de_la_classe` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `enseignants_classes`
--

INSERT INTO `enseignants_classes` (`id`, `identifiant_enseignant`, `nom_de_la_classe`) VALUES
(72, 'CBFG08PFM', '4ème'),
(73, 'CBFG03PFF', '6ème'),
(74, 'CBFG03PFF', '5ème'),
(75, 'CBFG03PFF', '4ème'),
(97, 'CBFG02PFF', '6ème'),
(98, 'CBFG02PFF', '5ème'),
(99, 'CBFG02PFF', '4ème'),
(100, 'CBFG05PFM', '6ème'),
(101, 'CBFG05PFM', '5ème'),
(102, 'CBFG05PFM', '4ème'),
(103, 'CBFG07PFF', '6ème'),
(104, 'CBFG07PFF', '5ème'),
(105, 'CBFG07PFF', '4ème'),
(106, 'CBFG10PFM', '6ème'),
(107, 'CBFG10PFM', '5ème'),
(108, 'CBFG10PFM', '4ème'),
(109, 'CBFG09PFM', '6ème'),
(110, 'CBFG09PFM', '5ème'),
(111, 'CBFG09PFM', '4ème'),
(112, 'CBFG04PFF', '6ème'),
(113, 'CBFG04PFF', '5ème'),
(114, 'CBFG04PFF', '4ème'),
(115, 'CBFG01PFF', '6ème'),
(116, 'CBFG01PFF', '5ème'),
(117, 'CBFG01PFF', '4ème'),
(118, 'CBFG08PFM', '6ème'),
(119, 'CBFG08PFM', '5ème'),
(120, 'CBFG08PFM', '4ème'),
(121, 'CBFG03PFF', '6ème'),
(122, 'CBFG03PFF', '5ème'),
(123, 'CBFG03PFF', '4ème'),
(124, 'CBFG03PAF', 'Form1'),
(125, 'CBFG03PAF', 'Form2'),
(126, 'CBFG03PAF', 'Form3'),
(127, 'CBFG04PAF', 'Form1'),
(128, 'CBFG04PAF', 'Form2'),
(129, 'CBFG04PAF', 'Form3'),
(130, 'CBFG01PAM', 'Form1'),
(131, 'CBFG01PAM', 'Form2'),
(133, 'CBFG06PAM', 'Form1'),
(134, 'CBFG06PAM', 'Form2'),
(135, 'CBFG06PAM', 'Form3'),
(136, 'CBFG07PAM', 'Form1'),
(137, 'CBFG07PAM', 'Form2'),
(138, 'CBFG07PAM', 'Form3'),
(141, 'CBFG05PAF', 'Form3'),
(142, 'CBFG02PAM', 'Form1'),
(143, 'CBFG02PAM', 'Form2'),
(144, 'CBFG02PAM', 'Form3'),
(145, 'CBFG11PFAM', '6ème'),
(146, 'CBFG11PFAM', '5ème'),
(147, 'CBFG11PFAM', '4ème'),
(148, 'CBFG11PFAM', 'Form1'),
(149, 'CBFG11PFAM', 'Form2'),
(150, 'CBFG11PFAM', 'Form3'),
(154, 'CBFG08PAM', 'Form1'),
(155, 'CBFG08PAM', 'Form2'),
(156, 'CBFG08PAM', 'Form3'),
(157, 'CBFG06PFM', '6ème'),
(158, 'CBFG06PFM', '5ème'),
(159, 'CBFG06PFM', '4ème'),
(160, 'CBFG01PAM', 'Form3'),
(161, 'CBFG09PAM', 'Form1'),
(162, 'CBFG09PAM', 'Form2'),
(163, 'CBFG09PAM', 'Form3');

-- --------------------------------------------------------

--
-- Structure de la table `matieres_des_enseignants`
--

CREATE TABLE `matieres_des_enseignants` (
  `identifiant_enseignant` varchar(50) DEFAULT NULL,
  `matiere_enseignee` varchar(255) DEFAULT NULL,
  `classe_specifique` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `matieres_des_enseignants`
--

INSERT INTO `matieres_des_enseignants` (`identifiant_enseignant`, `matiere_enseignee`, `classe_specifique`) VALUES
('CBFG02PFF', 'Anglais', NULL),
('CBFG05PFM', 'Latin', NULL),
('CBFG07PFF', 'Sciences', NULL),
('CBFG10PFM', 'Informatique', NULL),
('CBFG09PFM', 'Mathématiques', NULL),
('CBFG04PFF', 'Histoire', NULL),
('CBFG08PFM', 'Espagnol', NULL),
('CBFG03PFF', 'Economie Social et Familiale(ESF)', NULL),
('CBFG03PAF', 'English Language', NULL),
('CBFG03PAF', 'Food and Nutrition', NULL),
('CBFG03PAF', 'literature', NULL),
('CBFG04PAF', 'French', NULL),
('CBFG01PAM', 'Geography', NULL),
('CBFG08PAM', 'Physics', NULL),
('CBFG06PAM', 'Mathematics', NULL),
('CBFG07PAM', 'Chemistry', NULL),
('CBFG07PAM', 'Biology', NULL),
('CBFG05PAF', 'Economics', NULL),
('CBFG05PAF', 'Commerce', NULL),
('CBFG02PAM', 'Computer Sciences', NULL),
('CBFG06PFM', 'Langue et Culture Nationale', NULL),
('CBFG11PFAM', 'Sport', NULL),
('CBFG04PFF', 'Géographie', NULL),
('CBFG04PFF', 'Éducation Civique et Morale (ECM)', NULL),
('CBFG09PFM', 'Physique Chimie Technologie', '4ème'),
('CBFG01PFF', 'Expression ecrite/orale', NULL),
('CBFG01PFF', 'Correction orthographique', NULL),
('CBFG01PFF', 'Etude de texte', NULL),
('CBFG09PAM', 'Citizenship', 'Form1'),
('CBFG09PAM', 'Citizenship', 'Form2'),
('CBFG09PAM', 'Citizenship', 'Form3'),
('CBFG09PAM', 'History', 'Form3'),
('CBFG01PAM', 'History', 'Form1'),
('CBFG01PAM', 'History', 'Form2'),
(NULL, 'Travail manuel', '6ème'),
(NULL, 'Travail manuel', '5ème'),
(NULL, 'Travail manuel', '4ème'),
(NULL, 'Manual labour', 'Form1'),
(NULL, 'Manual labour', 'Form2'),
(NULL, 'Manual labour', 'Form3');

-- --------------------------------------------------------

--
-- Structure de la table `notes`
--

CREATE TABLE `notes` (
  `id` int(11) NOT NULL,
  `matricule_eleve` varchar(20) NOT NULL,
  `matiere` varchar(100) NOT NULL,
  `note` decimal(4,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `notes_annuelles`
--

CREATE TABLE `notes_annuelles` (
  `id` int(11) NOT NULL,
  `note_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `notes_sequentielles`
--

CREATE TABLE `notes_sequentielles` (
  `id` int(11) NOT NULL,
  `note_id` int(11) NOT NULL,
  `sequence` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `notes_trimestrielles`
--

CREATE TABLE `notes_trimestrielles` (
  `id` int(11) NOT NULL,
  `note_id` int(11) NOT NULL,
  `trimestre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `parents`
--

CREATE TABLE `parents` (
  `id` int(11) NOT NULL,
  `identifiant` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `presences`
--

CREATE TABLE `presences` (
  `id` int(11) NOT NULL,
  `matricule_eleve` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `heure_entree` time DEFAULT NULL,
  `heure_sortie` time DEFAULT NULL,
  `heures_absence` int(11) DEFAULT NULL,
  `decision` varchar(100) DEFAULT NULL,
  `minutes_retard` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `sequences`
--

CREATE TABLE `sequences` (
  `numero_de_sequence` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `sequences`
--

INSERT INTO `sequences` (`numero_de_sequence`) VALUES
(1),
(2),
(3),
(4),
(5),
(6);

-- --------------------------------------------------------

--
-- Structure de la table `trimestres`
--

CREATE TABLE `trimestres` (
  `numero_de_trimestre` int(11) NOT NULL,
  `date_de_debut` date NOT NULL,
  `date_de_fin` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `administrateur_principal`
--
ALTER TABLE `administrateur_principal`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `identifiant` (`identifiant`);

--
-- Index pour la table `administration`
--
ALTER TABLE `administration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `identifiant` (`identifiant`);

--
-- Index pour la table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`nom_de_la_classe`);

--
-- Index pour la table `eleves`
--
ALTER TABLE `eleves`
  ADD PRIMARY KEY (`matricule_eleve`);

--
-- Index pour la table `enseignants`
--
ALTER TABLE `enseignants`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `identifiant` (`identifiant`);

--
-- Index pour la table `enseignants_classes`
--
ALTER TABLE `enseignants_classes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `identifiant_enseignant` (`identifiant_enseignant`),
  ADD KEY `classe` (`nom_de_la_classe`);

--
-- Index pour la table `matieres_des_enseignants`
--
ALTER TABLE `matieres_des_enseignants`
  ADD KEY `identifiant_enseignant` (`identifiant_enseignant`),
  ADD KEY `fk_classe` (`classe_specifique`);

--
-- Index pour la table `notes`
--
ALTER TABLE `notes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `matricule_eleve` (`matricule_eleve`);

--
-- Index pour la table `notes_annuelles`
--
ALTER TABLE `notes_annuelles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `note_id` (`note_id`);

--
-- Index pour la table `notes_sequentielles`
--
ALTER TABLE `notes_sequentielles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `note_id` (`note_id`),
  ADD KEY `sequence` (`sequence`);

--
-- Index pour la table `notes_trimestrielles`
--
ALTER TABLE `notes_trimestrielles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `note_id` (`note_id`),
  ADD KEY `trimestre` (`trimestre`);

--
-- Index pour la table `parents`
--
ALTER TABLE `parents`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `identifiant` (`identifiant`);

--
-- Index pour la table `presences`
--
ALTER TABLE `presences`
  ADD PRIMARY KEY (`id`),
  ADD KEY `matricule_eleve` (`matricule_eleve`);

--
-- Index pour la table `sequences`
--
ALTER TABLE `sequences`
  ADD PRIMARY KEY (`numero_de_sequence`);

--
-- Index pour la table `trimestres`
--
ALTER TABLE `trimestres`
  ADD PRIMARY KEY (`numero_de_trimestre`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `administrateur_principal`
--
ALTER TABLE `administrateur_principal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `administration`
--
ALTER TABLE `administration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `enseignants`
--
ALTER TABLE `enseignants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=146;

--
-- AUTO_INCREMENT pour la table `enseignants_classes`
--
ALTER TABLE `enseignants_classes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=164;

--
-- AUTO_INCREMENT pour la table `notes`
--
ALTER TABLE `notes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=446;

--
-- AUTO_INCREMENT pour la table `notes_annuelles`
--
ALTER TABLE `notes_annuelles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `notes_sequentielles`
--
ALTER TABLE `notes_sequentielles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=446;

--
-- AUTO_INCREMENT pour la table `notes_trimestrielles`
--
ALTER TABLE `notes_trimestrielles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `parents`
--
ALTER TABLE `parents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `presences`
--
ALTER TABLE `presences`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT pour la table `sequences`
--
ALTER TABLE `sequences`
  MODIFY `numero_de_sequence` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `trimestres`
--
ALTER TABLE `trimestres`
  MODIFY `numero_de_trimestre` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `enseignants_classes`
--
ALTER TABLE `enseignants_classes`
  ADD CONSTRAINT `enseignants_classes_ibfk_1` FOREIGN KEY (`identifiant_enseignant`) REFERENCES `enseignants` (`identifiant`),
  ADD CONSTRAINT `enseignants_classes_ibfk_2` FOREIGN KEY (`nom_de_la_classe`) REFERENCES `classes` (`nom_de_la_classe`);

--
-- Contraintes pour la table `matieres_des_enseignants`
--
ALTER TABLE `matieres_des_enseignants`
  ADD CONSTRAINT `fk_classe` FOREIGN KEY (`classe_specifique`) REFERENCES `classes` (`nom_de_la_classe`),
  ADD CONSTRAINT `matieres_des_enseignants_ibfk_1` FOREIGN KEY (`identifiant_enseignant`) REFERENCES `enseignants` (`identifiant`);

--
-- Contraintes pour la table `notes`
--
ALTER TABLE `notes`
  ADD CONSTRAINT `notes_ibfk_1` FOREIGN KEY (`matricule_eleve`) REFERENCES `eleves` (`matricule_eleve`);

--
-- Contraintes pour la table `notes_annuelles`
--
ALTER TABLE `notes_annuelles`
  ADD CONSTRAINT `notes_annuelles_ibfk_1` FOREIGN KEY (`note_id`) REFERENCES `notes` (`id`);

--
-- Contraintes pour la table `notes_sequentielles`
--
ALTER TABLE `notes_sequentielles`
  ADD CONSTRAINT `notes_sequentielles_ibfk_1` FOREIGN KEY (`note_id`) REFERENCES `notes` (`id`),
  ADD CONSTRAINT `notes_sequentielles_ibfk_2` FOREIGN KEY (`sequence`) REFERENCES `sequences` (`numero_de_sequence`);

--
-- Contraintes pour la table `notes_trimestrielles`
--
ALTER TABLE `notes_trimestrielles`
  ADD CONSTRAINT `notes_trimestrielles_ibfk_1` FOREIGN KEY (`note_id`) REFERENCES `notes` (`id`),
  ADD CONSTRAINT `notes_trimestrielles_ibfk_2` FOREIGN KEY (`trimestre`) REFERENCES `trimestres` (`numero_de_trimestre`);

--
-- Contraintes pour la table `presences`
--
ALTER TABLE `presences`
  ADD CONSTRAINT `presences_ibfk_1` FOREIGN KEY (`matricule_eleve`) REFERENCES `eleves` (`matricule_eleve`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
