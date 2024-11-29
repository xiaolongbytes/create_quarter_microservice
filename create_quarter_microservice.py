"""
Given a starting quarter (Season + Year) and a graduating quarter (Season + Year)
Returns a JSON object of quarters between and inclusive of the provided quarters
"""

from flask import Flask, Response, request, jsonify
import json
import uuid

app = Flask(__name__)

@app.route('/create_quarters', methods=['POST'])
def create_quarters():
    payload = request.get_json()

    startSeason = payload['startSeason']
    startYear = payload['startYear']
    endSeason = payload['endSeason']
    endYear = payload['endYear']

    # Check if start quarter is before end quarter
    if startYear > endYear or (startYear == endYear and startSeason > endSeason):
        return Response(
            json.dumps({'message': 'Invalid inputs, start quarter is after graduation quarter'}),
            status=400,
            mimetype="application/json"
        )

    # Create Quarters
    quarters = []
    SEASON_TO_FRONTEND_SEASON_ENUM = ["WINTER", "SPRING", "SUMMER", "FALL"]

    FALL = 3
    WINTER = 0
    for year in range(startYear, endYear + 1):
        stop_season = endSeason if year == endYear else FALL
        begin_season = startSeason if year == startYear else WINTER
        for season in range(begin_season, stop_season + 1):
            quarters.append({'id': str(uuid.uuid4()), 'season': SEASON_TO_FRONTEND_SEASON_ENUM[season], 'year': year})
    return jsonify(quarters)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
