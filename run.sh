#!/bin/bash

# Fonction pour exécuter le test
run_test() {
    local script="$1"
    local input_file="$2"
    local output_file="$3"

    # Exécute le script python avec l'input et capture la sortie dans un fichier temporaire
    "./$script" < "$input_file" > temp_output.txt

    # Compare la sortie avec le fichier de sortie attendu
    if diff -wB temp_output.txt "$output_file" > /dev/null; then
        echo "Test $input_file -> $output_file: OK"
    else
        echo "Test $input_file -> $output_file: KO"
    fi
}

# Fonction pour parcourir les répertoires et exécuter les tests
run_all_tests() {
    for dir in 1 2 3 4 5; do
        # Vérifier s'il y a des fichiers Python dans le répertoire
        script=$(ls "$dir"/*.py 2>/dev/null)

        if [[ -n "$script" ]]; then
            sample_dir="$dir/sample"

            if [[ -d "$sample_dir" ]]; then
                input_files=($(ls "$sample_dir"/input*.txt | sort))
                output_files=($(ls "$sample_dir"/output*.txt | sort))

                for i in "${!input_files[@]}"; do
                    run_test "$script" "${input_files[i]}" "${output_files[i]}"
                done
            fi
            echo "========================================"
        fi
    done
}

# Lancer tous les tests
run_all_tests
