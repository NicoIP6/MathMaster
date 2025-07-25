from random import randint
from modules.StudyMaster.revision_master import Revision
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from matplotlib.patches import Rectangle

class SetTheory(Revision):
    def __init__(self, name):
        super().__init__(name)
        self.list_of_set = [{randint(0, 15) for i in range(1, randint(4, 10))} for i in range(randint(2,3))]

    def description_set(self):
        pass

# # Définir nos ensembles
# set1 = {"A", "B", "C"}
# set2 = {"C", "D", "E"}
#
# # Créer le diagramme de Venn
# plt.figure(figsize=(10, 6))
# v = venn2([set1, set2], ('Ensemble 1', 'Ensemble 2'))
#
# # Supprimer les étiquettes numériques automatiques
# for label in v.subset_labels:
#     if label is not None:
#         label.set_text('')
#
# # Ajouter nos propres étiquettes avec les lettres
# # Région unique à l'ensemble 1 (10)
# plt.annotate('A, B', xy=v.get_label_by_id('10').get_position(),
#              xytext=(0, 0), ha='center', textcoords='offset points')
#
# # Région d'intersection (11)
# plt.annotate('C', xy=v.get_label_by_id('11').get_position(),
#              xytext=(0, 0), ha='center', textcoords='offset points')
#
# # Région unique à l'ensemble 2 (01)
# plt.annotate('D, E', xy=v.get_label_by_id('01').get_position(),
#              xytext=(0, 0), ha='center', textcoords='offset points')
#
# # Ajouter un titre
# plt.title('Diagramme de Venn avec lettres')
#
# # Afficher le diagramme
# plt.tight_layout()
# plt.show()


#
# def venn_diagram_with_universal_set():
#     # Définir nos ensembles
#     ensemble_universel = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"}
#     ensemble1 = {"A", "B", "C", "D"}
#     ensemble2 = {"C", "D", "E", "F", "G"}
#
#     # Éléments qui ne sont dans aucun des ensembles (mais dans l'ensemble universel)
#     elements_outside = ensemble_universel - (ensemble1 | ensemble2)
#
#     # Créer une figure avec un fond gris clair pour représenter l'ensemble universel
#     fig, ax = plt.subplots(figsize=(12, 8))
#
#     # Dessiner un rectangle gris clair pour représenter l'ensemble universel
#     universal_rect = Rectangle((-1.2, -1.2), 2.4, 2.4, facecolor='#EEEEEE', edgecolor='black', linestyle='--')
#     ax.add_patch(universal_rect)
#
#     # Créer le diagramme de Venn
#     v = venn2([ensemble1, ensemble2], ('Ensemble A', 'Ensemble B'), ax=ax)
#
#     # Supprimer les étiquettes numériques automatiques
#     for label in v.subset_labels:
#         if label is not None:
#             label.set_text('')
#
#     # Ajouter nos propres étiquettes avec les éléments
#     # Région unique à l'ensemble 1 (10)
#     elements_only_in_1 = ensemble1 - ensemble2
#     plt.annotate(', '.join(sorted(elements_only_in_1)),
#                  xy=v.get_label_by_id('10').get_position(),
#                  xytext=(0, 0), ha='center', textcoords='offset points')
#
#     # Région d'intersection (11)
#     elements_in_both = ensemble1.intersection(ensemble2)
#     plt.annotate(', '.join(sorted(elements_in_both)),
#                  xy=v.get_label_by_id('11').get_position(),
#                  xytext=(0, 0), ha='center', textcoords='offset points')
#
#     # Région unique à l'ensemble 2 (01)
#     elements_only_in_2 = ensemble2 - ensemble1
#     plt.annotate(', '.join(sorted(elements_only_in_2)),
#                  xy=v.get_label_by_id('01').get_position(),
#                  xytext=(0, 0), ha='center', textcoords='offset points')
#
#     # Ajouter les éléments de l'ensemble universel qui ne sont dans aucun des deux ensembles
#     plt.annotate(f"Éléments hors des ensembles: {', '.join(sorted(elements_outside))}",
#                  xy=(-1.1, -1.1), xytext=(0, 0),
#                  ha='center', va='top', color='black')
#
#     # Ajouter le label pour l'ensemble universel
#     plt.annotate("Ensemble Universel Ω = {" + ', '.join(sorted(ensemble_universel)) + "}",
#                  xy=(-1.1, -1.1), xytext=(0, 0),
#                  ha='center', va='bottom', fontsize=12, fontweight='bold')
#
#     # Ajuster les limites des axes pour s'assurer que tout est visible
#     ax.set_xlim(-1.3, 1.3)
#     ax.set_ylim(-1.3, 1.3)
#
#     # Supprimer les axes
#     ax.axis('off')
#
#     plt.title('Diagramme de Venn avec Ensemble Universel')
#     plt.tight_layout()
#     plt.show()
#
#
# # Exécuter la fonction
# venn_diagram_with_universal_set()
