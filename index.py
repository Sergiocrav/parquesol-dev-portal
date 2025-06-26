# Portal do Desenvolvedor ParqueSol - Simplificado para Vercel
# Template HTML para o Portal do Desenvolvedor
PORTAL_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Portal do Desenvolvedor ParqueSol</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
            line-height: 1.6;
        }
        header { 
            background-color: #4CAF50; 
            color: white; 
            padding: 10px 20px; 
            border-radius: 5px;
        }
        section { 
            margin: 20px 0; 
            padding: 15px; 
            background-color: #f9f9f9; 
            border-radius: 5px;
        }
        code {
            background-color: #f1f1f1;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        .endpoint {
            background-color: #e9e9e9;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Portal do Desenvolvedor ParqueSol</h1>
    </header>
    
    <section>
        <h2>API de Energia Solar Distribuída</h2>
        <p>
            Bem-vindo ao Portal do Desenvolvedor ParqueSol. Esta API permite integrar dados 
            de geração solar e informações de usuários da plataforma ParqueSol em suas aplicações.
        </p>
    </section>
    
    <section>
        <h2>Endpoints Disponíveis</h2>
        
        <div class="endpoint">
            <h3>Geração Solar</h3>
            <code>GET /api/v1/generation</code>
            <p>Retorna dados de geração solar para um período específico.</p>
        </div>
        
        <div class="endpoint">
            <h3>Economia de Carbono</h3>
            <code>GET /api/v1/carbon-savings</code>
            <p>Calcula a redução de emissões de CO₂ baseada na geração solar.</p>
        </div>
        
        <div class="endpoint">
            <h3>Estatísticas da Comunidade</h3>
            <code>GET /api/v1/community-stats</code>
            <p>Retorna estatísticas agregadas da comunidade ParqueSol.</p>
        </div>
    </section>
    
    <section>
        <h2>Autenticação</h2>
        <p>
            Para utilizar esta API, você precisará de uma chave de API. 
            Para solicitar uma chave, acesse <a href="/api/portal/request-api-key">Solicitar Chave API</a>.
        </p>
    </section>
    
    <footer>
        <p>&copy; 2025 ParqueSol - Energia Solar Distribuída</p>
    </footer>
</body>
</html>
"""

# Formato específico para funções serverless da Vercel
def handler(event, context):
    """
    Handler para função serverless da Vercel.
    Processa requisições com base no path e retorna o conteúdo apropriado.
    """
    # Extrair o caminho da requisição
    path = event.get('path', '/')
    
    # Roteamento básico
    if path == '/':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': '{"status":"success","message":"ParqueSol Developer Portal API","version":"1.0","endpoints":["/api/portal/","/api/portal/my-keys","/api/portal/request-api-key","/api/docs/","/api/health"]}'
        }
    elif path == '/api/health':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': '{"status":"ok","service":"ParqueSol Developer Portal","version":"1.0","environment":"production"}'
        }
    elif path == '/api/portal/' or path == '/api/portal':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': PORTAL_TEMPLATE
        }
    elif path == '/api/portal/my-keys':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': 'Gerenciamento de Chaves API - ParqueSol (Em desenvolvimento)'
        }
    elif path == '/api/portal/request-api-key':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': 'Solicitar Nova Chave API - ParqueSol (Em desenvolvimento)'
        } 
    elif path == '/api/docs/' or path == '/api/docs':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': 'Documentação da API ParqueSol (Em desenvolvimento)'
        }
    else:
        return {
            'statusCode': 404,
            'headers': {'Content-Type': 'text/plain'},
            'body': '404 Not Found'
        }
