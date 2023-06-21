def generate_atom_code(atom):
    return f"createAtom('{atom['name']}', {atom['position']});"


def generate_js_code(scene_data):
    atom_code = [generate_atom_code(atom) for atom in scene_data]
    atom_code_str = "\n".join(atom_code)

    js_code = f'''
    <script src="https://cdn.jsdelivr.net/npm/three@0.131.0/build/three.min.js"></script>

    <script>
        function createAtom(name, position) {{
            var geometry = new THREE.SphereGeometry(0.2, 32, 32);
            var material = new THREE.MeshLambertMaterial({{ color: 'green' }});
            var sphere = new THREE.Mesh(geometry, material);
            sphere.position.set(position[0], position[1], position[2]);
            scene.add(sphere);
        }}

        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        var renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        var light = new THREE.DirectionalLight(0xffffff);
        light.position.set(10, 10, 10);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.z = 5;

        {atom_code_str}

        function animate() {{
            requestAnimationFrame(animate);
            scene.rotation.y += 0.01;
            renderer.render(scene, camera);
        }}

        animate();
    </script>
    '''

    return js_code


def generate_html_page(js_code):
    html_page = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>3D Model</title>
        <style>
            body {{
                margin: 0;
                overflow: hidden;
            }}
        </style>
    </head>
    <body>
        {js_code}
    </body>
    </html>
    '''

    return html_page


def generate_3d_model_file(scene_data, filename):
    js_code = generate_js_code(scene_data)
    html_page = generate_html_page(js_code)

    with open(filename, 'w') as file:
        file.write(html_page)

    print(f"HTML file '{filename}' has been generated.")
    return html_page