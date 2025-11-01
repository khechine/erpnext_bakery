# ERPNext Bakery Application

Application pour configurer automatiquement une boulangerie complète dans ERPNext.

## 🚀 Installation

1. **Copier l'application dans votre environnement ERPNext :**
   ```bash
   cp -r apps/erpnext_bakery /home/frappe/frappe-bench/apps/
   ```

2. **Installer l'application :**
   ```bash
   docker-compose exec erpnext bench --site erpnext.local install-app erpnext_bakery
   ```

3. **Redémarrer les services (optionnel) :**
   ```bash
   docker-compose restart erpnext
   ```

## 📋 Ce qui est inclus

### 🏷️ **Groupes d'articles (8)**
- Pains
- Viennoiseries
- Pâtisseries
- Gâteaux et Entremets
- Biscuits et Snacks
- Ingrédients
- Emballages
- Boissons et Suppléments

### 🛍️ **Articles (40)**
- **22 produits finis** : pains, viennoiseries, pâtisseries, gâteaux, biscuits, boissons
- **18 ingrédients** : farines, produits laitiers, sucres, chocolats, fruits, épices

### 🏭 **Nomenclatures (BOMs) (15)**
- Recettes détaillées pour chaque produit avec quantités précises
- Calcul automatique des coûts de production

### 👥 **Fournisseurs (8)**
- Minoterie Tunisienne
- Laiterie du Sahel
- Sucrerie Maghrébine
- Chocolaterie Carthage
- Fruits Frais Tunisia
- Emballages Modernes
- Café Tunis
- Épices & Aromates

### 🏪 **Profil POS**
- Configuration complète pour les ventes en caisse
- Interface optimisée pour boulangerie

## 💰 **Configuration financière**
- Devise : **TND (Tunisian Dinar)**
- TVA : 19%
- Comptes de vente, charges et trésorerie configurés

## 🔄 **Persistance des données**

Les données sont automatiquement chargées via :
- **Fixtures** : Chargement automatique lors de l'installation
- **Patches** : Mise à jour automatique lors des migrations

Toutes les données restent persistantes même après redémarrage Docker !

## 🎯 **Utilisation**

### **Production :**
1. Créer des ordres de production depuis les nomenclatures (BOMs)
2. Consommer les ingrédients depuis le stock
3. Produire les produits finis

### **Ventes :**
1. Utiliser le profil POS "Bakery POS" pour les ventes
2. Scanner ou sélectionner les articles
3. Calcul automatique des totaux avec TVA

### **Achats :**
1. Créer des factures d'achat depuis les fournisseurs
2. Réceptionner la marchandise
3. Mettre à jour automatiquement les stocks

## 📊 **Rapports disponibles**
- État des stocks par article
- Valeur totale du stock
- Mouvements de stock
- Ventes par période
- Rentabilité par produit

## 🔧 **Scripts de maintenance**

### **Recharger les données :**
```bash
docker-compose exec erpnext bench --site erpnext.local execute erpnext_bakery.scripts.load_bakery_items.load_bakery_items
```

### **Vider les données de test :**
```bash
docker-compose exec erpnext bench --site erpnext.local execute erpnext_bakery.scripts.load_bakery_items.reset_bakery_items
```

## 🌟 **Fonctionnalités clés**
- ✅ **Stock multi-entrepôt** avec suivi en temps réel
- ✅ **Gestion des nomenclatures** pour la production
- ✅ **Interface POS** optimisée pour la vente
- ✅ **Gestion des fournisseurs** et achats
- ✅ **Calcul automatique des coûts**
- ✅ **Support multidevise** (TND configuré)
- ✅ **Données persistantes** après redémarrage

---

**🇹🇳 Application développée pour les boulangeries tunisiennes**