</tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            {% for student in results %}
                            <tr>
                                <td class="p-3 font-mono text-xs text-slate-500">{{ student.id }}</td>
                                <td class="p-3 font-bold text-slate-900">{{ student.name }}</td>
                                <td class="p-3">{{ student.grade }}</td>
                                <td class="p-3 font-bold text-cyan-600">{{ student.gpa }}</td>
                                <td class="p-3"><span class="bg-emerald-100 text-emerald-800 text-xs px-2.5 py-1 rounded-full font-semibold">{{ student.status }}</span></td>s
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            {% else %}
                <p class="text-slate-500 text-sm text-center py-4">No student found with that name.</p>
            {% endif %}
        </div>
        {% endif %}
    </main>

    <footer class="py-6 text-center text-xs text-cyan-200/50">
        <p>&copy; 2026 Student Information System. All rights reserved.</p>
    </footer>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    query = request.args.get("query", "").strip()
    results = []
    if query:
        results = [s for s in STUDENTS if query.lower() in s["name"].lower() or query.lower() in s["id"].lower()]
    return render_template_string(HTML_TEMPLATE, query=query, results=results)s