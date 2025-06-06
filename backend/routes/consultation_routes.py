from flask import Blueprint, request, jsonify
from models.consultation_model import ConsultationModel
from neo_services.neo_consultation import NeoConsult

cons_bp = Blueprint("consult", __name__, url_prefix="/consultations")

@cons_bp.route("", methods=["POST"])
def create_consult():
    data = request.get_json()
    # On s'attend à ce que data contienne : date, description, patient_id, medecin_id
    cons_id = ConsultationModel.create(data)
    # Création des relations dans Neo4j
    NeoConsult.create_relations(
        cons_id=cons_id,
        patient_id=data["patient_id"],
        medecin_id=data["medecin_id"],
        date=data["date"],
        description=data["description"]
    )
    return jsonify({"_id": cons_id}), 201

@cons_bp.route("", methods=["GET"])
def get_all_consult():
    all_cons = ConsultationModel.find_all()
    for c in all_cons:
        c["_id"] = str(c["_id"])
    return jsonify(all_cons), 200

@cons_bp.route("/neo", methods=["GET"])
def get_all_consults_neo():
    all_cons = NeoConsult.get_all_consults_with_relations()
    return jsonify(all_cons), 200


@cons_bp.route("/<cons_id>", methods=["PUT"])
def update_consult(cons_id):
    data = request.get_json()
    updated = ConsultationModel.update(cons_id, data)
    if updated:
        return jsonify({"msg": "Consultation mise à jour"}), 200
    return jsonify({"error": "Non trouvé"}), 404

@cons_bp.route("/<cons_id>", methods=["DELETE"])
def delete_consult(cons_id):
    deleted = ConsultationModel.delete(cons_id)
    if deleted:
        NeoConsult.delete_relations(cons_id)
        return jsonify({"msg": "Consultation supprimée"}), 200
    return jsonify({"error": "Non trouvé"}), 404

