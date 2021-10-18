<script src="../main.js"></script>
<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-row justify="center">
          <v-col md="12">
            <v-card
                class="pa-3 my-5"
            >
              <v-card-title>개인정보 입력</v-card-title>

              <v-card-text class="py-7">
                <v-row>
                  <v-col cols="12" md="3"justify="center" align="center">
                    <video ref="register_video" style="width:100%;max-width:300px;" :src="register_video" controls></video>
                  </v-col>

                  <v-col cols="12" md="8">
                    <v-row>
                      <v-col>
                        <v-form
                            ref="form"
                            v-model="valid"
                        >
                          <v-text-field
                              v-model="name"
                              :counter="20"
                              label="이름"
                              :error-messages="nameErrors"
                              required
                          ></v-text-field>

                          <v-radio-group
                              label="성별"
                              v-model="sex"
                              :error-messages="sexErrors"
                              row
                          >
                            <v-radio
                                label="남"
                                value="male"
                            ></v-radio>
                            <v-radio
                                label="여"
                                value="female"
                            ></v-radio>
                            <v-radio
                                label="기타"
                                value="etc"
                            ></v-radio>
                          </v-radio-group>

                          <v-text-field
                              v-model="age"
                              label="나이"
                              :error-messages="ageErrors"
                              required
                          ></v-text-field>


                          <v-divider class="my-10"></v-divider>

                          <v-text-field v-model="disabled_degree" label="청각장애 정도 (dB)" :error-messages="disabledDegreeErrors"></v-text-field>
                          <v-radio-group
                              v-model="disabled_type"
                              row
                              label="청각장애 유형"
                              :error-messages="disabledTypeErrors"
                          >
                            <ul>
                              <v-radio
                                  label="보조기기를 착용하여도 말소리를 이해하지 못한다."
                                  value="A"
                              ></v-radio>
                              <v-radio
                                  label="보조기기를 착용하면 말소리만 이해할 수 있다."
                                  value="B"
                              ></v-radio>
                              <v-radio
                                  label="보조기기를 사용하면 음악 소리는 들린다."
                                  value="C"
                              ></v-radio>
                              <v-radio
                                  label="전혀 들리지 않는다."
                                  value="D"
                              ></v-radio>
                            </ul>
                          </v-radio-group>



                          <v-row><v-col>의사소통 수단 (*중복체크가능)</v-col></v-row>
                          <v-row>
                            <v-col>
                              <v-checkbox
                                  v-model="communication_type"
                                  label="수어"
                                  value="A"
                              ></v-checkbox>
                            </v-col>
                            <v-col>
                              <v-checkbox
                                  v-model="communication_type"
                                  label="필담"
                                  value="B"
                              ></v-checkbox>
                            </v-col>
                            <v-col>
                              <v-checkbox
                                  v-model="communication_type"
                                  label="구어"
                                  value="C"
                              ></v-checkbox>
                            </v-col>
                            <v-col cols="5">
                              <v-row>
                                <v-col cols="auto">
                                  <v-checkbox
                                      v-model="communication_type"
                                      label="기타"
                                      value="D"
                                  ></v-checkbox>
                                </v-col>
                                <v-col>
                                  <v-text-field v-model="communication_input" label="직접 입력해주세요." :disabled="!communication_type.includes('D')"></v-text-field>
                                </v-col>
                              </v-row>

                            </v-col>
                          </v-row>

                        </v-form>
                      </v-col>
                    </v-row>
                  </v-col>
                </v-row>

              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    :disabled="!valid"
                    color="success"
                    class="px-5"
                    large
                    @click="validate">
                  시작하기
                  <div v-show="showPing" class="ping"></div>
                </v-btn>
              </v-card-actions>
            </v-card>

          </v-col>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, maxLength, email } from 'vuelidate/lib/validators'

export default {
  name: "Register",
  mixins: [validationMixin],
  validations: {
    name: { required },
    sex: { required },
    age: { required },
    disabled_degree: { required },
    disabled_type: { required },

  },
  data: () => ({
    exp_description: '불러오는 중...',
    loading: false,
    valid: false,

    name: null,
    sex: null,
    age: null,
    disabled_type: null,
    disabled_degree: null,
    communication_type: [],
    communication_input: null,
  }),
  computed: {
    register_video: function () {
      return this.$utils.getApiUrl() + '/attachments/register.mp4'
    },

    sexErrors () {
      const errors = []
      if (!this.$v.sex.$dirty) return errors
      !this.$v.sex.required && errors.push('성별은 필수항목 입니다.')
      return errors
    },
    nameErrors () {
      const errors = []
      if (!this.$v.name.$dirty) return errors
      !this.$v.name.required && errors.push('이름은 필수항목 입니다.')
      return errors
    },
    ageErrors () {
      const errors = []
      if (!this.$v.name.$dirty) return errors
      !this.$v.age.required && errors.push('나이는 필수항목 입니다.')
      return errors
    },
    disabledDegreeErrors () {
      const errors = []
      if (!this.$v.name.$dirty) return errors
      !this.$v.disabled_degree.required && errors.push('청각장애 정도는 필수항목 입니다.')
      return errors
    },
    disabledTypeErrors () {
      const errors = []
      if (!this.$v.name.$dirty) return errors
      !this.$v.disabled_type.required && errors.push('청각장애 유형는 필수항목 입니다.')
      return errors
    },
    showPing: function () {
      if(this.name == null || this.name == '') return false
      if(this.sex == null) return false
      if(this.age == null || this.age == '') return false
      if(this.disabled_degree == null || this.disabled_degree == '') return false
      if(this.disabled_type.length == 0) return false
      if(this.communication_type.length == 0) return false
      return true
    }
  },
  mounted() {
    if(this.$cookies.get('user_id') != null) {
      // Already Login
      this.$router.push('/demo')
    }

    this.exp_description = ''

    axios.get(this.$utils.getApiUrl() + '/experiment-desc')
        .then((res) => { this.exp_description = res.data })
        .catch((ex) => { console.log('Connection error', ex); })
  },
  methods: {
    validate: function() {
      this.$v.$touch()
      if(this.$v.$invalid) { return }

      let self = this

      axios.post(this.$utils.getApiUrl() + '/register', {
        name: this.name,
        sex: this.sex,
        age: this.age,
        disabled_degree: this.disabled_degree,
        disabled_type: this.disabled_type,
        communication_type: this.communication_type,
        communication_input: this.communication_input
      })
      .then((res) => {
        this.$cookies.set('user_id', res.data);
        this.$cookies.set('name', self.name);
        location.reload()
      })
      .catch((ex) => { console.log('Connection error', ex); })

    }
  }
}
</script>

<style scoped>

</style>