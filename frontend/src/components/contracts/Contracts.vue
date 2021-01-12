<template>

  <div class="container">
   
          <p>Contracts List</p>         

          <table class="table table-bordered table-hover table-striped">
              <thead>
                <tr>
                  <th scope="col">id</th>
                  <th scope="col">Start Date</th>
                  <th scope="col">Updated</th>
                  <th scope="col">Number</th>
                  <th scope="col">PartnerId</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in list_contracts" :key="item.message">
                      <td>{{ item.id }}</td>
                      <td>{{ item.start_date }}</td>
                      <td>{{ item.updated }}</td>
                      <td>{{ item.number }}</td>
                      <td>{{ item.partner_id.name }}</td>
                </tr>               
              </tbody>
              </table>
           <!-- <button class="btn btn-link" @click="getContracts">Afiseaza</button> -->
   
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
// Import component
// import Loading from "vue-loading-overlay";
// Import stylesheet
// import "vue-loading-overlay/dist/vue-loading.css";

export default {
  data() {
    return {     
      isLoading: true,
      fullPage: true,
      tags: [],      
      token2: [],
      prefix: [],
      auth: [],    
      list_contracts: []
    };
  },
   computed: {
    ...mapGetters(["isLoggedIn", "authUser"])
  },
  methods: {    
    getContracts() {
      this.isLoading = false;
      this.token2 = this.$store.state.token;
      this.prefix = 'Token ';
      this.auth = `${this.prefix}${this.token2.auth_token}`;
      // console.log(this.auth);
      axios
        .get("/api/contracts", 
        { headers: { 
          'Authorization': this.auth
                   } 
        })
        .then(res => {
          this.list_contracts = res.data;
          console.log(res.data);
          this.isLoading = false;
        })
        .catch(error => {
          console.error(error);
          this.isLoading = false;
        });
    }
  },
  created() {
    this.getContracts();
  }
};
</script>

<style lang="css">
.btn {
  margin: 5px 5px;
}
</style>


