import web
import requests
import json
urls = (
    '/parametros?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros():
    def POST(self):
        try:
          parametros = web.input()
          texto=(parametros["texto"])
          key="2630acf0-a236-11eb-a050-53ad201312bb76778992-9d3d-4248-b403-ed7546e360e1"
          url="https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
          response = requests.get(url, params={ "data" : texto})
          if response.ok:
            responseData = response.json()
            topMatch = responseData[0]
            label = topMatch["class_name"]
            confidence = topMatch["confidence"]
            data = {}
            data["resultado: "] = label
            data["confianza: "] = confidence
            result = json.dumps(data)
            return result       
          else:
            response.raise_for_status()
        except:
          data = {}
          data["mensaje"] = "verifica los datos ingresados"
          return json.dumps(data)
if __name__ == "__main__":
    app.run()