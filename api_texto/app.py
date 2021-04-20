import web
import requests
import json
urls = (
    '/parametros?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros():
    def GET(self):
        try:
          def classify(text,texto):
              key ="285755f0-a214-11eb-a050-53ad201312bbb746a72c-fa08-4920-ac29-b6774420bca3"
              url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
              response = requests.get(url, params={ "data" : text })
              if response.ok:
                responseData = response.json()
                topMatch = responseData[0]
                return topMatch
              else:
                response.raise_for_status()
              #parametros = web.input()
              #texto= (parametros["texto"])
              demo = classify("tipos de billetes")
              label = demo["class_name"]
              confidence = demo["confidence"]
              #data = {}
              #data["resultado"] = label
              #data["confianza"] = confidence
              #result = json.dumps(data)
              #return result
              print ("result: '%s' with %d%% confidence" % (label, confidence)) 
        except:
          data = {}
          data["mensaje"] = "verifica los datos ingresados"
          return json.dumps(data)
if __name__ == "__main__":
    app.run()