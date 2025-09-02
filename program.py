import json

# Caminhos dos arquivos (ajuste se necessário)
caminho_following = "following.json"
caminho_followers = "followers_1.json"

# Carregar dados
with open(caminho_following, "r", encoding="utf-8") as f:
    following_data = json.load(f)

with open(caminho_followers, "r", encoding="utf-8") as f:
    followers_data = json.load(f)

# Extrair quem você segue
following = {
    entry["string_list_data"][0]["value"]
    for entry in following_data["relationships_following"]
    if "string_list_data" in entry and entry["string_list_data"]
}

# Extrair quem te segue (verifica o formato do JSON)
if isinstance(followers_data, dict) and "string_list_data" in followers_data:
    followers = {
        entry["value"]
        for entry in followers_data["string_list_data"]
    }
elif isinstance(followers_data, list):
    followers = set()
    for item in followers_data:
        if "string_list_data" in item:
            for entry in item["string_list_data"]:
                followers.add(entry["value"])
else:
    raise ValueError("Formato inesperado no arquivo followers_1.json")

nao_seguem_de_volta = sorted(following - followers)

# Exibir resultado
print("\n🔍 Pessoas que você segue mas que NÃO te seguem de volta:")
for nome in nao_seguem_de_volta:
    print("-", nome)

print(f"\n📌 Total: {len(nao_seguem_de_volta)} perfis")