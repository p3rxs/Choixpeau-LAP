const personnagesATester = [
    {"Courage": 9, "Ambition": 2, "Intelligence": 8, "Good": 9},
    {"Courage": 6, "Ambition": 7, "Intelligence": 9, "Good": 7},
    {"Courage": 3, "Ambition": 8, "Intelligence": 6, "Good": 3},
    {"Courage": 2, "Ambition": 3, "Intelligence": 7, "Good": 8},
    {"Courage": 3, "Ambition": 4, "Intelligence": 8, "Good": 8}
];

const k = 5;
function csvToTable(csvData) {
    const lines = csvData.split('\n');
    const table = [];
    const keys = lines[0].trim().split(';');
    for (let i = 1; i < lines.length; i++) {
        const line = lines[i].trim();
        if (line !== '') { // Skip empty lines
            const values = line.split(';');
            const record = {};
            for (let j = 0; j < keys.length; j++) {
                record[keys[j]] = values[j] ? values[j].trim() : null; // Trim values
            }
            table.push(record);
        }
    }

    return table;
}

function fusion_table(tabl1, tabl2) {
    /**
     * Rôle : fusionner les données brutes de deux fichiers CSV vers une liste
     * Entrée : chemin et nom des fichiers csv à traiter
     * Sortie : liste fusionnée
     */

    const poudlard = [];
    for (const poudlard_character of tabl1) {
        for (const kaggle_character of tabl2) {
            if (poudlard_character['Name'] === kaggle_character['Name']) {
                Object.assign(poudlard_character, kaggle_character);
                poudlard.push(poudlard_character);
            }
        }
    }
    return poudlard;
}

const poudlard_characters = fusion_table(csv_to_table("Caracteristiques_des_persos.csv"), csv_to_table("Characters.csv"));

function mesureDeDistance(fusionDeTable, persoTest) {
    for (const perso of fusionDeTable) {
        const distance = Math.sqrt(
            Math.pow(parseInt(perso["Courage"]) - persoTest["Courage"], 2) +
            Math.pow(parseInt(perso["Ambition"]) - persoTest["Ambition"], 2) +
            Math.pow(parseInt(perso["Intelligence"]) - persoTest["Intelligence"], 2) +
            Math.pow(parseInt(perso["Good"]) - persoTest["Good"], 2)
        );
        perso["Distance"] = distance;
    }
    fusionDeTable.sort((a, b) => a["Distance"] - b["Distance"]);
    return fusionDeTable;
}

function kProcheVoisins(fusionDeTable) {
    const kPlusProcheVoisins = [];
    let compteur = 0;
    for (const perso of fusionDeTable) {
        if (compteur < k) {
            kPlusProcheVoisins.push(perso);
            compteur++;
        }
    }
    return kPlusProcheVoisins;
}

function maisonDesVoisins(voisins) {
    const listeMaison = [
        ["Gryffindor", 0],
        ["Slytherin", 0],
        ["Ravenclaw", 0],
        ["Hufflepuff", 0]
    ];
    const listMaisonProche = voisins.map(voisin => voisin['House']);
    for (const maison of listMaisonProche) {
        switch (maison) {
            case "Gryffindor":
                listeMaison[0][1]++;
                break;
            case "Slytherin":
                listeMaison[1][1]++;
                break;
            case "Ravenclaw":
                listeMaison[2][1]++;
                break;
            case "Hufflepuff":
                listeMaison[3][1]++;
                break;
            default:
                break;
        }
    }
    listeMaison.sort((a, b) => b[1] - a[1]);
    return listeMaison;
}

function testePersoVoisins(listeDePoudlard, perso) {
    let listeMaison = [];
    // Suppression de la réaffectation de listeDePoudlard
    listeMaison = maisonDesVoisins(listeDePoudlard);
    if (listeMaison[0][1] === listeMaison[1][1]) {
        // Vérifiez si listeDePoudlard est vide avant d'accéder à ses éléments
        if (listeDePoudlard.length > 0 && (listeDePoudlard[0]["House"] === listeMaison[0][1] || listeDePoudlard[0]["House"] === listeMaison[1][1])) {
            perso["Maison"] = listeDePoudlard[0]["House"];
        } else if (listeDePoudlard.length > 1) { // Vérifiez si listeDePoudlard contient au moins deux éléments
            perso["Maison"] = listeDePoudlard[1]["House"];
        }
    } else if (listeMaison.length > 0) { // Vérifiez si listeMaison n'est pas vide
        perso["Maison"] = listeMaison[0][0];
    }
    return [listeDePoudlard, perso];
}


function affichageDesVoisins(perso, listeDePoudlard) {
    console.log(`Ce personnage a un courage de ${perso['Courage']}, une ambition de ${perso['Ambition']}, une intelligence de ${perso['Intelligence']}, une tendance à la bonté de ${perso['Good']},\nIl irait bien chez les ${perso['Maison']}`);
    console.log('Ses 5 plus proche voisins sont: ');
    for (const voisin of listeDePoudlard.slice(0, k)) {
        console.log(`${voisin['Name']}, ${voisin['House']}, ${voisin['Distance']}`);
    }
    console.log("\n");
}

function afficherResultats(profils, poudlardCharacters) {
    for (const perso of profils) {
        const [table, persoAvecMaison] = testePersoVoisins(poudlardCharacters, perso);
        affichageDesVoisins(persoAvecMaison, table);
    }
}
const nouveauxProfils = [
    {"Courage": 7, "Ambition": 6, "Intelligence": 5, "Good": 7},
    {"Courage": 5, "Ambition": 7, "Intelligence": 8, "Good": 6},
    {"Courage": 8, "Ambition": 3, "Intelligence": 9, "Good": 8}
];

afficherResultats(nouveauxProfils, poudlardCharacters);