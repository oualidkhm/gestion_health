from flask import Blueprint, request, jsonify
from models.rendezvous_model import RendezVousModel
from neo_services.neo_rendezvous import NeoRdv

rdv_bp = Blueprint("rdv", __name__, url_prefix="/rdv")

@rdv_bp.route("", methods=["POST"])
def create_rdv():
    try:
        data = request.get_json()
        rdv_id = RendezVousModel.create(data)
        NeoRdv.create_relations(
            rdv_id=rdv_id,
            patient_id=data["patient_id"],
            medecin_id=data["medecin_id"],
            date=data["date"],
            statut=data["statut"]
        )
        return jsonify({"_id": rdv_id}), 201
    except Exception as e:
        print("Erreur création RDV :", e)
        return jsonify({"error": str(e)}), 500


@rdv_bp.route("", methods=["GET"])
def get_all_rdv():
    all_rdv = RendezVousModel.find_all()
    # Convertir ObjectId en string pour chaque document
    for rdv in all_rdv:
        rdv["_id"] = str(rdv["_id"])
    return jsonify(all_rdv), 200

@rdv_bp.route("/<rdv_id>", methods=["PUT"])
def update_rdv(rdv_id):
    data = request.get_json()
    updated = RendezVousModel.update(rdv_id, data)
    if updated:
        return jsonify({"msg": "Rendez-vous mis à jour"}), 200
    return jsonify({"error": "Non trouvé"}), 404

@rdv_bp.route("/<rdv_id>", methods=["DELETE"])
def delete_rdv(rdv_id):
    deleted = RendezVousModel.delete(rdv_id)
    if deleted:
        NeoRdv.delete_relations(rdv_id)
        return jsonify({"msg": "Rendez-vous supprimé"}), 200
    return jsonify({"error": "Non trouvé"}), 404


# … existing POST, GET, PUT, DELETE …

@rdv_bp.route("/neo", methods=["GET"])
def get_all_rdv_neo():
    data = NeoRdv.get_all_rdv_with_relations()
    return jsonify(data), 200
